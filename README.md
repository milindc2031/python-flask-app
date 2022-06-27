# Python-flask-app

This repository contains simple python flask application with few endpoints and the Dcokerfile to package python app inside it.

Steps to setup the Pipeline are as Follows:

1. Install and configure Jenkins master slave on any server
2. Install below plugins to ensure the all functionalities required for the Pipeline
   - Docker
   - Github
   - Kubernetes plugin
   - Amazon EC2 plugin
   - Docker-build-Step
   - Github branch source plugins
   - etc

3. Configure Docker hub credentials
4. Configure Github secrets credentials
5. Configure Kubernetes configuration(kubeconfig)
6. Crate Multi-branch pipeline job
7. Configure git repository and setup poll scm frequency to every minute to ensure all commits are getting build OR setup Webhooks in the Github repository to jenkins URL.
8. Set Jenkinsfile path
9. Save the Jenkins job
10. Job will do initial scan of the repository and create pipeline for all branches which are having Jenkinsfile at the specified path
11. Jenkins jobs will be triggered and execute all the stages mentioned in the Jenkinsfile
