Pipeline{
    agent any

    stages{
        stage('Build') {
            steps {
                script {
                    docker.build('Test')
                }
            }
        }

        stage('Test') {
            steps {
                script{
                    def path = pwd().replaceAll('C:', 'c:').replaceAll('\\\\', '/')
                    bat "docker run -v ${path}:${path} -w ${path} test_assign pytest -v ./main.test.py"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def path = pwd().replaceAll('C:','c:').replaceAll('\\\\','/')
                    bat "docker run -v ${path}:${path} -w ${path} test_assign python main.py"
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