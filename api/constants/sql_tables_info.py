tables_info = {
    "vendedores": { "procedure": "vendedores_no_ventas" },
    "clientes": { "procedure": "clientes_no_ventas" },
}

carga_info = {
    "insertData": {
        "procedure_name": "CARGAR_DATA_MANUAL",
        "table_name": "CARGA_IM",
        "column_names": [
            'CODIGO_DISTRIBUIDOR',
            'FECHA',
            'FACTURA',
            'CODIGO_CLIENTE',
            'RUC',
            'RAZON_SOCIAL',
            'TIPO_NEGOCIO',
            'CODIGO_VENDEDOR',
            'DNI_VENDEDOR',
            'NOMBRE_VENDEDOR',
            'CODIGO_PRODUCTO',
            'DESCRIPCION_PRODUCTO',
            'CANTIDAD',
            'UNIDAD_MEDIDA',
            'PRECIO_UNITARIO',
            'PRECIO_SIN_IGV'
        ]
    }
}