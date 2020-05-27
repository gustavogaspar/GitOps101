# GitOps 101
Esta es una guía para principiantes quienes estan interesados en GitOps usando la nube de Oracle (Oracle Cloud Infraestructure)

En este tutorial se creará un flujo de desarrollo (development pipeline) completo usando un repositorio Git como guía para la ejecución de los "jobs". Primero se realizará la implementación de un Backend en Python, sobre un cluster de Kubernates usando un "job" manual, luego un flujo (pipeline) será creado y vinculado a un repositorio git para usar una actividad en git como disparador para actualizar el backend en Python.

## Requisitos Previos

* [Crear una cuenta Trial en Oracle Cloud Infraestructure](https://www.oracle.com/cloud/free/)
* [Crear un clauster de Kubernetes](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html)
* [Crear una instancia DevCS](https://docs.oracle.com/en/cloud/paas/developer-cloud/csdcs/service-setup.html#GUID-8EE9FC19-70A0-4508-A6B1-FB8425C13A91)
* [Recolección de  datos](./requiredinfos.md)

## Laboratorios

1. [Lab 100 - Crear un proyecto](Lab100/Lab100.md)
2. [Lab 200 - Crear un Build job](Lab200/Lab200.md)
3. [Lab 300 - Configurar Oracle Cloud Bash](Lab300/Lab300.md)
4. [Lab 400 - Crear un Job Deploy](Lab400/Lab400.md)
5. [Lab 500 - Crear un pipeline Automated](Lab500/Lab500.md)


##### Have Fun!!!
