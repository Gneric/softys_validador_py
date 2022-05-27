USE [STRATEGIO_CONTROL_SOFTYSI]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CARGA_IM](
	[CODIGO_DISTRIBUIDOR] [varchar](100) NULL,
	[FECHA] [int] NULL,
	[FACTURA] [varchar](100) NULL,
	[CODIGO_CLIENTE] [varchar](100) NULL,
	[RUC] [varchar](15) NULL,
	[RAZON_SOCIAL] [varchar](200) NULL,
	[TIPO_NEGOCIO] [varchar](100) NULL,
	[CODIGO_VENDEDOR] [varchar](100) NULL,
	[DNI_VENDEDOR] [varchar](15) NULL,
	[NOMBRE_VENDEDOR] [varchar](150) NULL,
	[CODIGO_PRODUCTO] [varchar](20) NULL,
	[DESCRIPCION_PRODUCTO] [varchar](200) NULL,
	[CANTIDAD] [decimal](14, 4) NULL,
	[UNIDAD_MEDIDA] [varchar](15) NULL,
	[PRECIO_UNITARIO] [decimal](14, 4) NULL,
	[PRECIO_SIN_IGV] [decimal](14, 4) NULL
) ON [PRIMARY]
GO