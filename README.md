# GitOps 101
Esta es una guía para principiantes que estén interesados ​​en GitOps utilizando Oracle Cloud Infraestructure

En este tutorial, se creará una tubería de desarrollo completo utilizando un repositorio Git como guía para la ejecución de los trabajos. Al principio, se implementará un backend de Python en un clúster de kubernetes utilizando trabajos manuales, luego se creará una tubería y se vinculará al repositorio de git, para usar las actividades de git como desencadenante para actualizar el backend de Python.

## Requistos Previos- 

* [Crear una instancia en Oracle Cloud Infraestructure Trial](https://www.oracle.com/cloud/free/)
* [Crear un clúster de Kubernetes](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html)
* [Crear una instancia de DevCS](https://docs.oracle.com/en/cloud/paas/developer-cloud/csdcs/service-setup.html#GUID-8EE9FC19-70A0-4508-A6B1-FB8425C13A91)
* [Recolectando los datos requeridos](./requiredinfos.md)

## Labs 

1. [Lab 100 - Creación de un proyecto](Lab100/Lab100.md)
2. [Lab 200 - Crear un Build job](Lab200/Lab200.md)
3. [Lab 300 - Configurar Oracle Cloud Bash](Lab300/Lab300.md)
4. [Lab 400 - Crear un Deploy job](Lab400/Lab400.md)
5. [Lab 500 - Crear un Automated pipeline](Lab500/Lab500.md)


##### ¡¡¡Que te Diviertas!!!
