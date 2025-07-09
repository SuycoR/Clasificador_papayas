import React, { useEffect, useState } from 'react';

export default function UltimaFoto() {
  const [prediccion, setPrediccion] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const obtenerPrediccion = () => {
    fetch('http://192.168.0.9:5000/api/resultado')
      .then((res) => {
        if (!res.ok) throw new Error('Error en la respuesta del servidor');
        return res.json();
      })
      .then((data) => {
        if (data.status === 'no_data') {
          setError('Aún no se ha tomado ninguna foto.');
          setPrediccion(null);
        } else {
          const nombreClase = getNombreClase(data.clase);
          const probabilidades = Array.isArray(data.probs?.[0])
            ? data.probs[0].map((p: number) => p.toFixed(4)).join(', ')
            : 'N/A';
          setPrediccion(`${nombreClase} | Probs: ${probabilidades}`);
          setError(null);
        }
      })
      .catch((err) => {
        console.error('❌ Error:', err);
        setError('No se pudo obtener la predicción.');
      });
  };

  useEffect(() => {
    obtenerPrediccion();

    // Opcional: auto-actualizar cada 5 segundos
    const interval = setInterval(() => {
      obtenerPrediccion();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const getNombreClase = (clase: number): string => {
    switch (clase) {
      case 0:
        return 'Papaya madura';
      case 1:
        return 'Papaya parcialmente madura';
      case 2:
        return 'Papaya verde';
      default:
        return 'Clase desconocida';
    }
  };

  return (
    <div style={{ display: 'flex', gap: '1rem' }}>
      <div>
        <h5>Última foto tomada:</h5>
        <img
           src={`http://192.168.0.9:5000/api/conseguirfoto?timestamp=${Date.now()}`}
          alt="Última foto"
          style={{ width: '200px', border: '1px solid gray' }}
        />
      </div>
      <div>
        <h5>Predicción:</h5>
        {error ? (
          <p style={{ color: 'red' }}>{error}</p>
        ) : (
          <p>{prediccion}</p>
        )}
      </div>
    </div>
  );
}
