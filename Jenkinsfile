pipeline {
  
  agent any
  
  parameters {
    string(name: 'ENVIRONMENT', defaultValue: 'Development', description: 'In which environment do you want to deploy the application?')
  }
  
  stages {
    stage('Testing') {
      parallel {
        stage('Unit Testing') {
          steps {
            echo "Running Unit Tests...."
//             sh "C:/Users/Function/AppData/Local/Programs/Python/Python38-32/python.exe -m unittest -v module-test"
          }
        }
        stage ('Integration Testing') {
          steps {
            echo "Running integration tests...."
          }
        }
      }
    }
    stage('Build') {
      steps {
        echo "Building executable file...."
      }
    }
    stage('Deploy') {
      steps {
        echo "Deploying app in ${params.ENVIRONMENT}"
      }
    }
  }
}
