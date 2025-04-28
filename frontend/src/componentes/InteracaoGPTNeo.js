import React, { useState } from 'react';
import axios from 'axios';

function InteracaoGPTNeo() {
  const [prompt, setPrompt] = useState('');
  const [resposta, setResposta] = useState('');
  const [carregando, setCarregando] = useState(false);

  const enviarPrompt = async () => {
    if (!prompt.trim()) {
      alert('Por favor, insira um prompt válido.');
      return;
    }
    setCarregando(true);
    setResposta('');
    try {
      const res = await axios.post('http://localhost:8000/api/gpt-neo/gerar', {
        prompt,
        max_length: 100,
        temperature: 0.7,
        top_p: 0.9,
      });
      setResposta(res.data.texto_gerado);
    } catch (error) {
      setResposta('Erro ao conectar com a API: ' + error.message);
    }
    setCarregando(false);
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h2 className="text-xl font-bold mb-4">Interação com GPT-Neo</h2>
      <textarea
        rows="5"
        className="w-full p-2 border rounded mb-4"
        placeholder="Digite seu prompt aqui..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button
        onClick={enviarPrompt}
        disabled={carregando}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {carregando ? 'Enviando...' : 'Enviar'}
      </button>
      <div className="mt-4 p-2 border rounded min-h-[100px] whitespace-pre-wrap bg-gray-50">
        {resposta}
      </div>
    </div>
  );
}

export default InteracaoGPTNeo;
