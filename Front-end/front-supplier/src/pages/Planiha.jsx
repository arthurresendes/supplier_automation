import React, { useState } from 'react'
import { planilhaConsumo } from '../api/planilhaConsumo'

const Planiha = () => {
    const [planilha, setPlanilha] = useState(null)
    const [dadosJson, setDadosJson] = useState(null)
    const [nome, setNome] = useState('')
    const [erro, setErro] = useState('')

    const lidarArquivo = (e) => {
        const arq = e.target.files[0]
        if (!arq) return

        setPlanilha(arq)
        setNome(arq.name)
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const respos = await planilhaConsumo(planilha)
            setDadosJson(respos)
        } catch (error) {
            setErro(error.message)
        }
    }


    return (
        <div>
            <form action="" method="post" onSubmit={handleSubmit}>
                <label htmlFor="planilha">
                    <input type="file" name="planilha" id="planilha" accept='.csv, .xlsx' onChange={lidarArquivo} />
                </label>
                {nome !== '' && (
                    <div>
                        <p>Nome do arquivo selecionado é: {nome}</p>
                    </div>
                )}
                <input type="submit" value="Validar" />
            </form>
            {erro && <p style={{ color: 'red', fontWeight: 'bold' }}>⚠️ {erro}</p>}
            {dadosJson && (
                <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
                    <thead>
                        <tr style={{ textAlign: 'left', backgroundColor: 'f2f2f2' }}>
                            <th>Matricula</th>
                            <th>Nome</th>
                            <th>Valor</th>
                            <th>Ação</th>
                        </tr>
                    </thead>
                    <tbody>
                        {dadosJson.map((dad) => (
                            <tr key={dad.Matricula} style={{ borderBottom: '1px solid #ddd' }}>
                                <td>{dad.Matricula}</td>
                                <td>{dad.Colaborador}</td>
                                <td>{dad.Valor}</td>
                                <td><button>Abrir chamado</button></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    )
}

export default Planiha