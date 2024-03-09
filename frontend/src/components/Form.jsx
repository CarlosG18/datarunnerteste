import '../css/form.css'
import Button from './Button'

function Form(){
    return (
        <>  
            <h1>Informe Seus Dados</h1>
            <form action="">
                <label htmlFor="title">titulo</label>
                <input id='title' type="text"/>
                <label htmlFor="dados">Dados</label>
                <input className='text-area' id='dados' type="text" />
                <Button acao={"enviar dados"}></Button>
            </form>
        </>
    )
}

export default Form;