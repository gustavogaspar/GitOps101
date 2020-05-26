# Antes de que empieces
## Este tutorial de 10 minutos le muestra cómo:

* Crear un nuevo clúster con configuraciones predeterminadas y nuevos recursos de redcrear un grupo de nodos

* Configurar el archivo kubeconfig para el clúster

* Verifique que puede acceder al clúster utilizando kubectl y el Panel de control de Kubernetes

## Antecedentes

Oracle Cloud Infrastructure Container Engine para Kubernetes es un servicio totalmente gestionado, escalable y de alta disponibilidad que puede utilizar para implementar sus aplicaciones en contenedores en la nube. Use Container Engine para Kubernetes cuando su equipo de desarrollo quiera construir, implementar y administrar de manera confiable aplicaciones nativas de la nube. Usted especifica los recursos informáticos que requieren sus aplicaciones, y Container Engine for Kubernetes los aprovisiona en Oracle Cloud Infrastructure en una tenencia de OCI existente.

En este tutorial, utiliza la configuración predeterminada para definir un nuevo clúster. Cuando crea el nuevo clúster, los nuevos recursos de red para el clúster se crean automáticamente, junto con un grupo de nodos y tres nodos de trabajadores privados. Luego configurará el archivo de configuración de Kubernetes para el clúster (el archivo 'kubeconfig' del clúster). El archivo kubeconfig le permite acceder al clúster utilizando kubectl y el Panel de control de Kubernetes.

Tenga en cuenta que en este tutorial, configurará el archivo kubeconfig para dar acceso al clúster desde su entorno de desarrollo local. Sin embargo, también puede configurar el archivo kubeconfig para dar acceso desde el entorno Cloud Shell (consulte el tema Configuración del acceso al clúster en la documentación del motor de contenedor para Kubernetes).

## ¿Que necesitas?

* Un nombre de usuario y contraseña de Oracle Cloud Infrastructure.

* Dentro de su arrendamiento, ya debe haber un compartimento para contener los recursos de red necesarios (VCN, subredes, puerta de enlace a Internet, puerta de enlace NAT, tabla de rutas, listas de seguridad). Si dicho compartimento aún no existe, deberá crearlo antes de comenzar este tutorial.

* Al menos tres instancias de proceso deben estar disponibles en la tenencia para completar este tutorial como se describe. Tenga en cuenta que si solo hay una instancia de proceso disponible, es posible crear un clúster con un grupo de nodos que tenga una sola subred y un solo nodo en el grupo de nodos. Sin embargo, dicho clúster no estará altamente disponible.

* Para crear y / o administrar clústeres, debe pertenecer a uno de los siguientes:

    * El grupo de Administradores del arrendamiento.
    * Un grupo al que una política otorga el Motor de contenedor apropiado para los permisos de Kubernetes. Como creará y configurará un       clúster y los recursos de red asociados durante el tutorial, las políticas también deben otorgar al grupo los permisos adecuados         sobre esos recursos.
    
* Antes de configurar el archivo kubeconfig más adelante en el tutorial, ya debe haber hecho lo siguiente:
    * generó un par de claves de firma API
    * agregó el valor de clave pública del par de claves de firma de API a la Configuración de usuario para su nombre de usuario
    * instaló y configuró la CLI de Oracle Cloud Infrastructure (versión 2.6.4 o posterior)

* Debe haber instalado y configurado la herramienta de línea de comandos Kubernetes kubectl. Si aún no lo ha hecho, [consulte la documentación de kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
