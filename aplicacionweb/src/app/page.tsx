"use client";

import { useState } from "react";
import { Camera, BarChart3, Clock, TrendingUp, ExternalLink, Activity, Zap, Eye } from "lucide-react";

// Componentes
import LiveCamera from "@/../components/LiveCamara";
import UltimaFoto from "@/../components/UltimaFoto";
import Navbar from "@/../components/Navbarr";

export default function Page() {
  // Estados
  const [fotoUrl, setFotoUrl] = useState("/placeholder.jpg");
  const [prediccion, setPrediccion] = useState("Sin predicción");

  // Función para abrir ThingSpeak
  const abrirThingSpeak = () => {
    window.open('https://thingspeak.mathworks.com/channels/3003644', '_blank');
  };

  return (
    <>
      <Navbar />
      
      <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900">
        {/* Header con título del dashboard */}
        <div className="bg-gradient-to-r from-slate-800 to-slate-900 shadow-2xl border-b border-gray-700">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <div className="p-2 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg shadow-lg">
                  <Camera className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h1 className="text-2xl lg:text-3xl font-bold text-white">
                    Dashboard de Monitoreo
                  </h1>
                  <p className="text-sm text-gray-300 mt-1">
                    Sistema de análisis y clasificación en tiempo real
                  </p>
                </div>
              </div>
              <div className="hidden sm:flex items-center gap-2 bg-gradient-to-r from-green-500/20 to-emerald-500/20 backdrop-blur-sm px-4 py-2 rounded-lg border border-green-500/30">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                <span className="text-sm font-medium text-green-300">Sistema Activo</span>
              </div>
            </div>
          </div>
        </div>

        {/* Contenido principal */}
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">
            
            {/* Columna izquierda - Cámara en vivo */}
            <div className="space-y-8">
              <div className="bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden backdrop-blur-sm">
                <div className="bg-gradient-to-r from-blue-600 to-blue-700 px-6 py-5">
                  <h2 className="text-xl font-bold text-white flex items-center">
                    <Camera className="w-6 h-6 text-blue-200 mr-3" />
                    Cámara en Vivo
                  </h2>
                </div>
                <div className="p-6 bg-gradient-to-b from-gray-800/50 to-gray-900">
                  <LiveCamera />
                </div>
              </div>

              {/* Panel de control rápido */}
              <div className="bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden backdrop-blur-sm">
                <div className="bg-gradient-to-r from-cyan-600 to-cyan-700 px-6 py-5">
                  <h2 className="text-xl font-bold text-white flex items-center">
                    <Zap className="w-6 h-6 text-cyan-200 mr-3" />
                    Control del Sistema
                  </h2>
                </div>
                <div className="p-6 bg-gradient-to-b from-gray-800/50 to-gray-900">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="flex items-center justify-between p-4 bg-gradient-to-r from-gray-700/50 to-gray-800/50 rounded-lg border border-gray-600">
                      <div className="flex items-center gap-3">
                        <Eye className="w-5 h-5 text-blue-400" />
                        <span className="text-white font-medium">Detección</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span className="text-sm text-green-300">Activo</span>
                      </div>
                    </div>
                    <div className="flex items-center justify-between p-4 bg-gradient-to-r from-gray-700/50 to-gray-800/50 rounded-lg border border-gray-600">
                      <div className="flex items-center gap-3">
                        <Activity className="w-5 h-5 text-purple-400" />
                        <span className="text-white font-medium">Procesamiento</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span className="text-sm text-green-300">En línea</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Columna derecha */}
            <div className="space-y-8">
              {/* Última foto */}
              <div className="bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden backdrop-blur-sm">
                <div className="bg-gradient-to-r from-purple-600 to-purple-700 px-6 py-5">
                  <h2 className="text-xl font-bold text-white flex items-center">
                    <TrendingUp className="w-6 h-6 text-purple-200 mr-3" />
                    Última Clasificación
                  </h2>
                </div>
                <div className="p-6 bg-gradient-to-b from-gray-800/50 to-gray-900">
                  <UltimaFoto fotoUrl={fotoUrl} prediccion={prediccion} />
                </div>
              </div>

              {/* Panel de análisis y estadísticas */}
              <div className="bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden backdrop-blur-sm">
                <div className="bg-gradient-to-r from-orange-600 to-orange-700 px-6 py-5">
                  <h2 className="text-xl font-bold text-white flex items-center">
                    <BarChart3 className="w-6 h-6 text-orange-200 mr-3" />
                    Análisis y Estadísticas
                  </h2>
                </div>
                <div className="p-6 bg-gradient-to-b from-gray-800/50 to-gray-900">
                  <div className="text-center space-y-6">
                    <div className="bg-gradient-to-r from-gray-700/30 to-gray-800/30 rounded-xl p-6 border border-gray-600">
                      <div className="flex items-center justify-center mb-4">
                        <div className="p-3 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-full">
                          <BarChart3 className="w-8 h-8 text-blue-400" />
                        </div>
                      </div>
                      <h3 className="text-lg font-semibold text-white mb-2">
                        Visualización Avanzada
                      </h3>
                      <p className="text-gray-300 text-sm mb-4">
                        Accede a gráficos detallados, históricos y análisis completos de los datos recolectados
                      </p>
                      <button
                        onClick={abrirThingSpeak}
                        className="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-medium py-3 px-6 rounded-lg transition-all duration-200 shadow-lg hover:shadow-xl transform hover:-translate-y-1"
                      >
                        <ExternalLink className="w-5 h-5" />
                        Abrir ThingSpeak
                      </button>
                    </div>
                    
                    <div className="grid grid-cols-2 gap-4">
                      <div className="bg-gradient-to-r from-emerald-500/10 to-emerald-600/10 rounded-lg p-4 border border-emerald-500/20">
                        <div className="text-2xl font-bold text-emerald-400 mb-1">24/7</div>
                        <div className="text-sm text-gray-300">Monitoreo</div>
                      </div>
                      <div className="bg-gradient-to-r from-cyan-500/10 to-cyan-600/10 rounded-lg p-4 border border-cyan-500/20">
                        <div className="text-2xl font-bold text-cyan-400 mb-1">Real</div>
                        <div className="text-sm text-gray-300">Tiempo</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Sección inferior - Información del sistema */}
          <div className="mt-8 bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden backdrop-blur-sm">
            <div className="bg-gradient-to-r from-indigo-600 to-indigo-700 px-6 py-5">
              <h2 className="text-xl font-bold text-white flex items-center justify-between">
                <div className="flex items-center">
                  <Clock className="w-6 h-6 text-indigo-200 mr-3" />
                  Estado del Sistema
                </div>
                <div className="flex items-center bg-white/20 backdrop-blur-sm text-white px-3 py-1 rounded-full text-sm font-medium shadow-lg">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full mr-2 animate-pulse"></div>
                  Operativo
                </div>
              </h2>
            </div>
            <div className="p-6 bg-gradient-to-b from-gray-800/50 to-gray-900">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="text-center p-4 bg-gradient-to-r from-gray-700/30 to-gray-800/30 rounded-lg border border-gray-600">
                  <div className="text-3xl font-bold text-green-400 mb-2">98.5%</div>
                  <div className="text-sm text-gray-300">Precisión del Sistema</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-r from-gray-700/30 to-gray-800/30 rounded-lg border border-gray-600">
                  <div className="text-3xl font-bold text-blue-400 mb-2">125ms</div>
                  <div className="text-sm text-gray-300">Tiempo de Respuesta</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-r from-gray-700/30 to-gray-800/30 rounded-lg border border-gray-600">
                  <div className="text-3xl font-bold text-purple-400 mb-2">24/7</div>
                  <div className="text-sm text-gray-300">Disponibilidad</div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}