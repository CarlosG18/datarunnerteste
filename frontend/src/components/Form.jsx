import '../css/form.css'
import Button from './Button'
import React, {useState} from 'react';

function Form(){
    const [title, setTitle] = useState('');
    const [dados, setDados] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('http://127.0.0.1:8000/treino/receber_dados', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, dados })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Erro:', error));
    };

    return (
        <>  
            <h1>Informe Seus Dados</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="title">titulo</label>
                <input id='title' type="text" value={title}
                onChange={(e) => setTitle(e.target.value)}/>
                <label htmlFor="dados">Dados</label>
                <input className='text-area' id='dados' type="text" value={dados}
                onChange={(e) => setDados(e.target.value)}/>
                <Button acao={"enviar dados"}></Button>
            </form>
            
        </>
    )
}

export default Form;