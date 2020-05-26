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

## 1 Iniciando OCI

1- En un navegador, iniciar sesión en Oracle Cloud Infrastructure.

![image](https://user-images.githubusercontent.com/54222755/82903031-ba3f9180-9f36-11ea-88d3-fa73056a82e8.png)
[Descripcion de la Imagen](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/files/oci-login-page.txt)

## 2 Definir detalles del clúster

1- En la consola, abra el menú de navegación. En Soluciones y plataforma , vaya a Servicios para desarrolladores y haga clic en            Clústeres de contenedores.

2- Elija un compartimento en el que tenga permiso para trabajar y en el que desee crear tanto el nuevo clúster como los recursos de red    asociados.

![image](https://user-images.githubusercontent.com/54222755/82903509-6e411c80-9f37-11ea-912f-e15a86dd7b6b.png)
[Descripción de la Imagen](https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/files/oci-console-create-cluster.txt)

3- En la página Clústeres , haga clic en Crear clúster.

4- En el cuadro de diálogo Crear clúster , haga clic en Creación rápida y haga clic en Iniciar flujo de trabajo .

![image](https://user-images.githubusercontent.com/54222755/82903837-f1627280-9f37-11ea-9df5-d96deba2ebdd.png)

5- En la página Crear clúster , cambie el valor del marcador de posición en el campo Nombre e ingrese en su Tutorial Cluster lugar.
![image](https://user-images.githubusercontent.com/54222755/82904210-85ccd500-9f38-11ea-8649-9ba5c4814439.png)

6- Haga clic en Siguiente para revisar los detalles que ingresó para el nuevo clúster.
![image](https://user-images.githubusercontent.com/54222755/82904349-ba409100-9f38-11ea-880b-a0e5fc69e9ea.png)

7- En la página Revisar , haga clic en Crear clúster para crear los nuevos recursos de red y el nuevo clúster.
Verá los diferentes recursos de red que se crean para usted.
![image](https://user-images.githubusercontent.com/54222755/82904419-d7755f80-9f38-11ea-92af-407eb59fed5d.png)

8- Haga clic en Cerrar para volver a la consola.
![image](https://user-images.githubusercontent.com/54222755/82904709-3935c980-9f39-11ea-80ad-ac093762e6bc.png)

El nuevo clúster se muestra en la página Detalles del clúster . Cuando se ha creado, el nuevo clúster tiene un estado de Activo

![image](https://user-images.githubusercontent.com/54222755/82904773-4eaaf380-9f39-11ea-9726-48cf7d2e042f.png)

9- En Recursos , seleccione Grupos de nodos y haga clic en el nombre del grupo de nodos en el clúster que acaba de crear (grupo1). En Recursos , seleccione Nodos y desplácese hacia abajo para ver los detalles de los nuevos nodos de trabajo (instancias de proceso) en el grupo de nodos.

