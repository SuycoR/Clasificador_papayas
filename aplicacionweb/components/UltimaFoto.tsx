type Props = {
  fotoUrl: string;
  prediccion: string;
};

export default function UltimaFoto({ fotoUrl, prediccion }: Props) {
  return (
    <div style={{ display: 'flex', gap: '1rem' }}>
      <div>
        <h5>Ultima foto tomada:</h5>
        <img
          src={"http://192.168.0.9:5000/foto"}
          alt="Última foto"
          style={{ width: '200px', border: '1px solid gray' }}
        />
      </div>
      <div>
        <h5>Predicción:</h5>
        <p>{prediccion}</p>
      </div>
    </div>
  );
}
// UltimaFoto.tsx
// Este componente muestra la última foto tomada y la predicción del modelo.