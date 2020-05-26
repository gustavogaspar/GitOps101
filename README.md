# GitOps 101
This is a beginners guide for those who are interested on GitOps using the Oracle Cloud Infraestructure

In this this tutorial a full develpment pipeline will be created using a Git Repository as a guideline for the execution of the jobs. At first a Python backend will be deployed on a kubernetes cluster using manual jobs, then a pipeline will be created, and linked to the git repository, to use git activities as a trigger to update the Python backend.

## Prerequisites - 

* [Creating a Oracle Cloud Infraestructure Trial](https://www.oracle.com/cloud/free/)
* [Creating a Kubernetes Cluster](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html)
* [Creating a DevCS instance](https://docs.oracle.com/en/cloud/paas/developer-cloud/csdcs/service-setup.html#GUID-8EE9FC19-70A0-4508-A6B1-FB8425C13A91)
* [Collecting the required data](./requiredinfos.md)

## Labs 

1. [Lab 100 - Creating a project](Lab100/Lab100.md)
2. [Lab 200 - Creating a Build job](Lab200/Lab200.md)
3. [Lab 300 - Configuring Oracle Cloud Bash](Lab300/Lab300.md)
4. [Lab 400 - Creating a Deploy job](Lab400/Lab400.md)
5. [Lab 500 - Creating an Automated pipeline](Lab500/Lab500.md)


##### Have Fun!!!
