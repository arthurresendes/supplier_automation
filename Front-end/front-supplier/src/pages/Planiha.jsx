import React, { useState } from 'react'
import { planilhaConsumo } from '../api/planilhaConsumo'
import { abrirChamado } from '../api/abrirChamado'
import styles from './planilha.module.css'

const Planiha = () => {
    const [planilha, setPlanilha] = useState(null)
    const [dadosJson, setDadosJson] = useState(null)
    const [nome, setNome] = useState('')
    const [erro, setErro] = useState('')
    const [carregando, setCarregando] = useState(false)
    const [ritm, setRitm] = useState('')
    const [colaborador, setColaborador] = useState('')
    const [solicitante, setSolicitante] = useState('')

    const lidarArquivo = (e) => {
        const arq = e.target.files[0]
        if (!arq) return

        setPlanilha(arq)
        setNome(arq.name)
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        setErro('')
        try {
            const respos = await planilhaConsumo(planilha)
            setDadosJson(respos)
        } catch (error) {
            setErro(error.message)
        }
    }

    const openDesk = async (solicitante, valor, colaborador, matricula) => {
        setErro('')
        setColaborador('')
        setSolicitante('')
        setRitm('')
        const dados = {
            Solicitante: solicitante,
            Valor: valor,
            Colaborador: colaborador,
            Matricula: matricula
        }
        setCarregando(true)
        try {
            const respos = await abrirChamado(dados)
            setRitm(respos)
        } catch (error) {
            setErro(error.message)
        } finally {
            setCarregando(false)
            setColaborador(colaborador)
            setSolicitante(solicitante)
        }
    }

    return (
        <div className={styles.container}>
            <form action="" method="post" onSubmit={handleSubmit} className={styles.form}>
                <label htmlFor="planilha" className={styles.fileLabel}>
                    Escolher arquivo
                    <input type="file" name="planilha" id="planilha" accept='.csv, .xlsx' onChange={lidarArquivo} className={styles.fileInput} />
                </label>
                {nome !== '' && (
                    <div>
                        <p className={styles.fileName}>Nome do arquivo selecionado é: {nome}</p>
                    </div>
                )}
                <input type="submit" value="Validar" className={styles.submitBtn} />
            </form>
            {erro && <p className={styles.errorMsg}>⚠️ {erro}</p>}

            {carregando && (
                <p className={styles.loadingMsg}>Abrindo chamado....</p>
            )}
            {ritm !== '' && (
                <p className={styles.successMsg}>Aberto o chamado para: {colaborador}. Solicitante: {solicitante}. RITM: {ritm}</p>
            )}
            {dadosJson && (
                <div className={styles.tableContainer}>
                    <table className={styles.table}>
                        <thead>
                            <tr>
                                <th>Matricula</th>
                                <th>Nome</th>
                                <th>Solicitante</th>
                                <th>Valor</th>
                                <th>Ação</th>
                            </tr>
                        </thead>
                        <tbody>
                            {dadosJson.map((dad) => (
                                <tr key={dad.Matricula}>
                                    <td>{dad.Matricula}</td>
                                    <td>{dad.Colaborador}</td>
                                    <td>{dad.Solicitante}</td>
                                    <td>{dad.Valor}</td>
                                    <td>
                                        {carregando ? (
                                            <button disabled className={styles.actionBtnDisabled}>Abrindo um chamado</button>
                                        ) : (
                                            <button onClick={() => openDesk(dad.Solicitante, dad.Valor, dad.Colaborador, dad.Matricula)} className={styles.actionBtn}>Abrir chamado</button>
                                        )}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    )
}

export default Planiha