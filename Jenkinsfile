// def branch = "main"
// def git_auth = "Zhang-abab_SHH"
// def git_address = "git@github.com:Zhang-abab/Project.git"
node{
    stage('拉取代码'){ 
       checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Zhang-abab-SSH', url: 'git@github.com:Zhang-abab/Project.git']]])
    }
    stage('切换目录'){ 
        //sh"su root"
        //sh"cd /home/Project"
        //sh"docker-compose stop"
        //sh"pwd"
        //sh"docker-compoes up"
    }
    stage('替换项目并运行'){ 
       sh"sudo rm -rf /home/Project/*"
       sh"sudo cp -r /var/lib/jenkins/workspace/Django_Yolo/* /home/Project"
       sh"docker-compose -f /home/Project/docker-compose.yml up"
    }
    echo '构建完成'
}

