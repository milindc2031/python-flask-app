pipeline {
agent any
options {
		skipStagesAfterUnstable()
}

stages {
	stage('Git clone') {
		steps {
    	sh 'echo "Cloning the repo"'
			sh 'git clone https://github.com/milindc2031/python-flask-app.git'
		  }
 	}

 	stage('Test') {
 		steps {
			sh '##python test_app.py'
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

	stage('Deliver for development') {
  	when {
          branch 'development'
          }
          steps {
                sh 'kubectl apply -f deployment.yaml'
            		}
  }

	stage('Deploy for production') {
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
