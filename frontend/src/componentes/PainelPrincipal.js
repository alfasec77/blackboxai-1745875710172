import React from 'react';

function PainelPrincipal() {
  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Painel Principal - Agente Mano DEV</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">Status da VM</h2>
          <p>CPU: 15%</p>
          <p>RAM: 4GB / 16GB</p>
          <p>Disco: 120GB / 256GB</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">Atalhos</h2>
          <ul className="list-disc list-inside">
            <li><a href="/gpt-neo" className="text-blue-600 hover:underline">Chat GPT-Neo</a></li>
            <li><a href="/scripts" className="text-blue-600 hover:underline">Execução de Scripts</a></li>
            <li><a href="/treinamento" className="text-blue-600 hover:underline">Gerenciamento de Treinamento</a></li>
            <li><a href="/configuracao" className="text-blue-600 hover:underline">Configurações</a></li>
            <li><a href="/registros" className="text-blue-600 hover:underline">Monitoramento de Logs</a></li>
          </ul>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">Informações Gerais</h2>
          <p>Versão do Sistema: 1.0.0</p>
          <p>Última Atualização: 2025-04-26</p>
          <p>Desenvolvedor: Mano DEV IA</p>
        </div>
      </div>
    </div>
  );
}

export default PainelPrincipal;
