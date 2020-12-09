from github import Github
from git import Repo
import os
import shutil
import subprocess


def api_limit():
    rate_limit = gh.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')


def build_query(keywords, languages):
    if keywords != '':
        keyword = [keyword.strip() for keyword in keywords.split(',')]
        query = '+'.join(keyword) + '+in:readme+in:description'
    else:
        language = [language.strip() for language in languages.split(',')]
        query = 'language:' + '+'.join(language)

    print('Query = ' + query)

    return query


def execute_query(query, sort, type_of_sort, max_size):
    result = gh.search_repositories(query, sort, type_of_sort)
    if result.totalCount > max_size:
        result = result[:max_size]

    return result


def get_repo(query_result, max_size):
    counter_index = 0
    for repo in query_result:
        counter_index += 1
        return_code_sonar = return_code_compiler = return_code_download = 0

        # find metrics for repository
        branch_count = repo.get_branches().totalCount
        contributor_count = repo.get_contributors().totalCount
        commit_count = repo.get_commits().totalCount
        release_count = repo.get_releases().totalCount

        print(f'{counter_index} / {max_size} : {repo.clone_url} ; {repo.name} ; {repo.language} ; '
              f'{repo.size} ; True ; {contributor_count}; {branch_count}; {commit_count} ; {release_count}')

        # Excluded project if (too big to scan) or language is null
        if repo.size < 650000 and repo.language is not None:
            path_repo = work_dir + repo.name

            if download_repository:
                return_code_download = \
                    download_folder(path_repo, repo.clone_url, repo.name, contributor_count)

            if execute_compiler:
                return_code_compiler = execute_gradlew(path_repo)

            if execute_sonarqube:
                return_code_sonar = execute_sonar(path_repo)

            print(f'Download = {return_code_download} ; Compiler = {return_code_compiler} ; '
                  f'Sonar = {return_code_sonar}')

        else:
            print(f'Exclusion = True (size > 650k, = None)')

        log_file.write(f'{repo.clone_url};{repo.name};{repo.language};{repo.size};'
                       f'{contributor_count};{branch_count};{commit_count};{release_count};'
                       f'{return_code_download};{return_code_compiler};{return_code_sonar}\n')


def download_folder(path_repo, url, name, contrib_count):
    return_code = 0
    if not os.path.exists(path_repo):
        try:
            Repo.clone_from(url, path_repo)
        except:
            return -1
        finally:
            if os.path.exists(path_repo):
                create_file_sonarqube(path_repo, name, contrib_count)
                copy_file(path_repo, 'local.properties')
                copy_file(path_repo, 'gradlew.bat')
                copy_file(path_repo, 'sonar.bat')
                return_code = 1

    return return_code


def create_file_sonarqube(path_repo, name, contrib_count):
    f = open(path_repo + '\\sonar-project.properties', 'w')
    f.write(f'sonar-project.properties\n')
    f.write(f'sonar.projectKey={name}\n')
    f.write(f'sonar.scm.provider=git\n')
    f.write(f'sonar.java.binaries=.\n')
    f.write(f'sonar.projectVersion={contrib_count}\n')
    f.close()


def execute_gradlew(path_repo):
    return_code = 0

    # Verification if already compile
    if os.path.exists(path_repo) and not os.path.exists(path_repo + "\\compilation_done.txt"):
        f_out = open(path_repo + '\\out_gradle.txt', 'w')
        rc = subprocess.run([path_repo + '\\gradlew.bat'], stdout=f_out, stderr=f_out, cwd=path_repo)
        f_out.close()

        if rc.returncode == 0:
            f = open(path_repo + '\\compilation_done.txt', 'w')
            f.close()

        return_code = rc.returncode

    return return_code


def execute_sonar(path_repo):
    return_code = 0

    # Verification is already scan
    if os.path.exists(path_repo) and not os.path.exists(path_repo + "\\sonar_done.txt"):
        f_out = open(path_repo + '\\out_sonar.txt', 'w')
        rc = subprocess.run([path_repo + '\\sonar.bat'], stdout=f_out, stderr=f_out, cwd=path_repo)
        f_out.close()

        if rc.returncode == 0:
            f = open(path_repo + '\\sonar_done.txt', 'w')
            f.close()

        return_code = rc.returncode

    return return_code


def copy_file(path_repo, name):
    source = work_compile_dir + '\\' + name
    target = path_repo + '\\' + name
    # if not path.exists(target):
    shutil.copyfile(source, target)


if __name__ == '__main__':
    # your github token
    token = 'your token'

    # Search - sample size
    max_size_project = 650
    # specific keyword
    keywords_project = ""
    # kotlin or python
    language_project = "Kotlin"
    # sort by stars, forks, updated
    sort_by = 'stars'
    # desc or asc
    sort_type = 'desc'

    # Configuration
    download_repository = True
    execute_sonarqube = True

    # future usage
    execute_compiler = False

    # Other configuration
    work_compile_dir = os.environ['PYTHONPATH'] + "\\Autres"
    work_dir = "your work dir"

    # logging
    log_name = 'log_repo.csv'
    log_file = open(work_dir + log_name, 'w')

    # main
    gh = Github(token)
    api_limit()
    build_query = build_query(keywords_project, language_project)
    result_query = execute_query(build_query, sort_by, sort_type, max_size_project)
    get_repo(result_query, max_size_project)
    log_file.close()
