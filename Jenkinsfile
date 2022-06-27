pipeline {
agent any
options {
		skipStagesAfterUnstable()
}

stages {
	stage('Git clone') {
		steps {
    	sh 'echo "Cloning the repo"'
		  }
 	}

 	stage('Test') {
 		steps {
			sh 'python test_app.py'
			}
	}

  stage('Dockerize the app') {
		steps {
			script{
	    	docker.withRegistry('https://index.docker.io/v1/', 'docker-creds') {
        def customImage = docker.build("chaudharimilind07/python-flsk-app:${env.BUILD_ID}")
        /* Push the container to  Registry */
        customImage.push()
				customImage.push('latest')
				}
    	}
		}
	}

	stage('Deploying on Dev env') {
  	when {
          branch 'development'
          }
          steps {
                sh 'kubectl apply -f deployment.yaml'
            		}
  }

	stage('Deploying on Production env') {
  	when {
          branch 'production'
          }
          steps {
                sh 'kubectl apply -f deployment.yaml'
                }
  }
}

post {
		always {
			echo 'The pipeline completed'
			junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
		}
		success {
			echo "Flask Application Up and running!!"
		}
		failure {
			echo 'Pipeline execution failed'
			error('Stopping early…')
		}
	}
}
