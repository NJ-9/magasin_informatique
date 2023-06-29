pipeline{
    agent any
        stages{
            stage('git checkout'){
                steps{
                    git credentialsId: '3624e941-6bdb-44d0-8f50-c80c5f5d6106', url: 'https://github.com/NJ-9/magasin_informatique'
                }
            }
            stage('Build the application'){
                steps{
                    bat 'mvn clean install'
                }
            }
            stage('Unit Test execution') {
                steps{
                    bat 'mvn test'
                }
            }
            stage("Build the docker image"){
                steps{
                    powershell "docker build -t euphoria776/pipeline-triangle ."
                }
            }
            stage('Push the docker image'){
                steps{
                    withCredentials([string(credentialsId:'75804f92-908e-456d-ad30-f1dc501ea25b', variable:'dockerHubPass')]){
                    powershell "docker login -u euphoria776 -p $dockerHubPass"
                    }
                    powershell "docker push euphoria776/pipeline-triangle"
                }
            }
        }
}
