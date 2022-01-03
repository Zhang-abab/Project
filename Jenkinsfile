def branch = "main"
def git_auth = "Zhang-abab_SHH"
def git_address = "git@github.com:Zhang-abab/Project.git"
node{
    stage('拉取代码'){ 
        checkout(
            [$class: 'GitSCM', 
            branches: [[name: '*/${branch}']], 
            userRemoteConfigs: [[credentialsId: "${git_auth}", 
            url: "${git_address}"]]])
    }
    stage('切换目录'){ 
        sh "cd /home/Project"
        sh "docker-compose stop"
    }
    echo '项目已停止'
}

