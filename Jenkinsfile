// def branch = "main"
// def git_auth = "Zhang-abab_SHH"
// def git_address = "git@github.com:Zhang-abab/Project.git"
node{
    stage('拉取代码'){ 
       checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Zhang-abab-SSH', url: 'git@github.com:Zhang-abab/Project.git']]])
    }
    stage('替换项目并运行'){ 
       sh"rm -rf /home/Project/*"
       sh"cp -r /var/lib/jenkins/workspace/Django_Yolo/* /home/Project"
       sh"chmod u+x /home/Project/run.sh"
       sh"/home/Project/run.sh"
    }
    echo '构建完成'
}

