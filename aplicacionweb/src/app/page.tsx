"use client";

import LiveCamera from "@/../components/LiveCamara";
import ResumenDiario from "@/../components/ResumenDiario";
import ClasificacionChart from "@/../components/ClasificacionChart";
import HistorialProcesamiento from "@/../components/HistorialProcesamiento";
import UltimaFoto from "@/../components/UltimaFoto";
import Navbar from "@/../components/Navbarr";
import { useState } from "react";

export default function Page() {
  const [fotoUrl, setFotoUrl] = useState("/placeholder.jpg");
  const [prediccion, setPrediccion] = useState("Sin predicción");

  // Aquí podrías tener lógica para actualizar `fotoUrl` y `prediccion` al presionar un botón

  return (
    <>
      <Navbar />
      <main style={{ display: "flex", padding: "20px", gap: "1rem" }}>
        {/* Columna izquierda */}
        <div style={{ flex: 1 }}>
          <LiveCamera />
          <UltimaFoto fotoUrl={fotoUrl} prediccion={prediccion} />
        </div>

        {/* Columna derecha */}
        <div style={{ flex: 1 }}>
          {/* Resumen y chart en fila */}
          <div style={{ display: "flex", gap: "1rem", marginBottom: "20px" }}>
            <ResumenDiario />
            <ClasificacionChart />
          </div>

          {/* Historial debajo */}
          <div>
            <HistorialProcesamiento />
          </div>
        </div>
      </main>
    </>
  );
}