// def branch = "main"
// def git_auth = "Zhang-abab_SHH"
// def git_address = "git@github.com:Zhang-abab/Project.git"
node{
    stage('拉取代码'){ 
       checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Zhang-abab-SSH', url: 'git@github.com:Zhang-abab/Project.git']]])
    }
    stage('切换目录'){ 
        sh"cd /home/Project"
        //sh"docker-compose stop"
    }
    stage('替换项目并运行'){ 
        sh"rm -rf ./*"
        sh"cp /var/lib/jenkins/workspace/Django_Yolo/* ./"
        sh"docker-compose up"
    }
    echo '构建完成'
}

