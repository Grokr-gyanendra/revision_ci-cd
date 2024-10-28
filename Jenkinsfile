pipeline{
    agent any

    stages{
        stage('Build') {
            steps {
                script {
                    docker.build('practice')
                }
            }
        }

        stage('Test') {
            steps {
                script{
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} practice pytest -v main_test.py"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def path = pwd().replaceAll('C:','/c').replaceAll('\\\\','/')
                    bat "docker run -v ${path}:${path} -w ${path} practice python main.py"
                }
            }
        }
    }

    post {
        success{
            echo "Deployed Successfully"
        }

        failure{
            echo "Failed Deployment"
        }
    }
}