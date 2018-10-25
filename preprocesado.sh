#!/bin/bash
args=("$@")
  if [ -f $1 ]; then
    out_traspon=${args/.csv/T_mv.csv}
    python traspon.py $args $out_traspon
    echo "Tabla traspuesta con éxito en $out_traspon"

    out_missingv=${out_traspon/T_mv.csv/T.csv}
    python missing_v.py $out_traspon $out_missingv
    echo "Missing values eliminados con éxito en $out_missingv"

    out_volatility=${out_missingv/T.csv/TV.csv}
    python colVol.py $out_missingv $out_volatility
    echo "Añadida columna de volatilidad en $out_volatility"

    out_escalado="escalado.csv"
    python escalado.py $out_volatility $out_escalado
    echo "Datos escalados (StandardScaler) con éxito en $out_escalado"

    out_diff="diff.csv"
    python diff.py $out_escalado $out_diff
    echo "Diferencias calculadas con éxito en $out_diff"
  fi
