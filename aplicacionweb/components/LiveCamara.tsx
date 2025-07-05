export default function LiveCamera() {
  return (
    <div>
      <h3>--------------------CAMARA EN VIVO--------------------</h3>
      <img
        src="http://192.168.0.9:5000/video_feed"
        alt="Cámara en vivo"
        style={{ width: '100%', maxWidth: '500px', border: '2px solid gray' }}
      />
    </div>
  );
}
