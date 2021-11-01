# HABI.CO - API

## Introducción

+ [Python 3.6.8](https://www.python.org/downloads/release/python-368/).
+ La API se creo con el framework [Flask](https://flask.palletsprojects.com/en/2.0.x/)
+ La conexion a la base de datos se logra 
    con la libreria [PyMySQL](https://pymysql.readthedocs.io/en/latest/).
+ Para las pruebas unitarias se utilizo la libreria [Unitest](https://pypi.org/project/unittest2/) y la aplicacion Postman.    

## Prerequisitos

+ Instala [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

Habilitar entorno virtual de 
Python y luego instalar las dependencias del proyecto.

```commandline
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```
## Uso
El proyecto está configurado para ejecutarse en el puerto 5000 del localhost o 127.0.0.1:5000.

```commandline
python manage.py runserver
```

El endpoint para consumir el servicio es:

```commandline
POST http://127.0.0.1:5000/habi-api/api/v1/prop/fil/
```

JSON con los datos que se esperan que
lleguen del front con los filtros solicitados por el usuario:

```commandline
{	
	"status": "pre_venta",
	"year": 2020,
	"city": "bogota"
}
```
Respuesta del servicio:
```commandline
    {
        "address": "calle 95 # 78 - 49",
        "city": "bogota",
        "status": "pre_venta",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar"
    }
```

## Pruebas Unitarias

+ Postman.

![alt text](https://github.com/jmelo77/Reto_Habi/blob/main/documentation/test_postman_habi_list_properties.png)

+ Unitest.

![alt text](https://github.com/jmelo77/Reto_Habi/blob/main/documentation/unitest_endpoints.png)


## Segundo Punto

Se propone el siguiente modelo de base de datos:

![alt text](https://github.com/jmelo77/Reto_Habi/blob/main/documentation/Diagram_ER_habi_db.png)

+ Código MySQL

/*
SQLyog Ultimate v8.71 
MySQL - 5.5.5-10.4.14-MariaDB : Database - habi_db
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`habi_db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `habi_db`;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Table structure for table `property` */

DROP TABLE IF EXISTS `property`;

CREATE TABLE `property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(120) NOT NULL,
  `city` varchar(32) NOT NULL,
  `price` bigint(20) NOT NULL,
  `description` text DEFAULT NULL,
  `year` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Table structure for table `property_user_like` */

DROP TABLE IF EXISTS `property_user_like`;

CREATE TABLE `property_user_like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `like` tinyint(1) NOT NULL,
  `date_like` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_property_user_like` (`property_id`),
  KEY `FK_property_user_like2` (`user_id`),
  CONSTRAINT `FK_property_user_like` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_property_user_like2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `status` */

DROP TABLE IF EXISTS `status`;

CREATE TABLE `status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `label` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status_historial_name_uindex` (`name`),
  UNIQUE KEY `status_historial_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Table structure for table `status_history` */

DROP TABLE IF EXISTS `status_history`;

CREATE TABLE `status_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `update_date` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `status_historial_id_uindex` (`id`),
  KEY `status_historial_property_id_fk` (`property_id`),
  KEY `status_historial_status_id_fk` (`status_id`),
  CONSTRAINT `status_historial_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
  CONSTRAINT `status_historial_status_id_fk` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

- Se incluye la tabla property_user_like para guardar los 'Me gusta'
de los usuarios, con una relación entre la tabla de property y la tabla auth_user.

## Propuestas futuras 

+ Adicionar autenticación con token JWT
+ Utilizar almacenamiento en cache Redis para que sean guardadas las consultas mas recurrentes y asi ganar mayor desempeño en la aplicación.
+ Utilizar la libreria SQLAlchemy ORM y aprovechar todas las ventajas de su uso.
+ Implementar más pruebas unitarias.

