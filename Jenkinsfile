// def branch = "main"
// def git_auth = "Zhang-abab_SHH"
// def git_address = "git@github.com:Zhang-abab/Project.git"
node{
    stage('拉取代码'){ 
       checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Zhang-abab_SHH', url: 'git@github.com:Zhang-abab/Project.git']]])
    }
    stage('切换目录'){ 
        sh"exit"
        sh"docker-compose stop"
    }
    echo '项目已停止'
}

