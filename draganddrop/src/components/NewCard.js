
const NewCard = ({value, setValue,setClick, addingHandle}) => {
    

    const submitHandle = (e) => {
        e.preventDefault();
        const newItem = {
            id: value.id,
            task: e.target.value
        }
        setValue({value:newItem});
        setClick(false);
        addingHandle();
    }
    const handleInput = (e) => {
        setValue(
            {id:value.id,
            title: e.target.value
            });
    }
    return (
        <div className='card'>
            <input type='text' 
            placeholder="Task" 
            value={value.title} 
            onChange={handleInput}/>
            <button className="btn-new" onClick={submitHandle}>Ekle</button>

        </div>
    )
}

export default NewCard