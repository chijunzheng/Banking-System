 pipeline {
   agent any

   stages {
     stage('Checkout') {
       steps {
         git branch: 'main', url: 'https://github.com/user/repo.git'
       }
     }

     stage('Build') {
       steps {
         sh 'make build'
       }
     }

     stage('Test') {
       steps {
         sh 'make test'
       }
     }

     stage('Dockerize') {
       steps {
         sh 'make docker'
       }
     }

     stage('Push') {
       steps {
         withCredentials([dockerUsernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
           sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
         }
         sh 'make push'
       }
     }
   }
 }

