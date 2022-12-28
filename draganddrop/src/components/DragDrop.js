//Droppable= objenin içinde hareket edebileceği alan oluşturur
//provide = objelerin bilgileri ve referansları içerir
//droppableProps = hareketi ve lokasyonunu takip etmek
//snapshot = bir anlık görüntü bağımsız değişkeni dahil olmak üzere iki bağımsız değişken iletebilir, 

import React, { useState } from 'react'
import { DragDropContext, Draggable, Droppable } from 'react-beautiful-dnd'
import storeData from '../store'
import Cards from './Cards';
import { v4 as uuidv4 } from 'uuid';
import NewCard from './NewCard';

const DragDrop = () => {
  const [data, setData] = useState(storeData);
  const [click, setClick] = useState(false);
  const [value, setValue] = useState({
    id: uuidv4(),
    title: ''
  }
  );
  const todo = ' 📃 To do'

  const onDragEnd = (result) => {
    if (!result.destination) return;
    const { source, destination } = result;

    if (source.droppableId !== destination.droppableId) {
      const sourceColIndex = data.findIndex(e => e.id === source.droppableId)
      const destinationColIndex = data.findIndex(e => e.id === destination.droppableId)

      const sourceCol = data[sourceColIndex]
      const destinationCol = data[destinationColIndex]

      const sourceTask = [...sourceCol.tasks]
      const destinationTask = [...destinationCol.tasks]

      const [removed] = sourceTask.splice(source.index, 1)
      destinationTask.splice(destination.index, 0, removed)

      data[sourceColIndex].tasks = sourceTask
      data[destinationColIndex].tasks = destinationTask

      setData(data)
    }
  }
  const addingHandle = () => {
    data[0].tasks.splice(0, 0, value)
    setData(data)
  }

  const onClickHandle = () => {
    setClick(true);
  }

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className='table'>
        {
          data.map(item => (
            <Droppable key={item.id} droppableId={item.id}>
              {(provided) => (
                <div {...provided.droppableProps}
                  className="section"
                  ref={provided.innerRef}
                >
                  <div className='title'>
                    {item.title}
                    {(item.title === todo) ? <span className='btn-add' style={{ float: 'right' }} onClick={onClickHandle}>+</span> : null}
                  </div>
                  <div className='context'>
                    {(click & item.title === todo) ? <NewCard value={value} setValue={setValue} setClick={setClick} addingHandle={addingHandle} /> : null}

                    {item.tasks.map((task, index) => (
                      <Draggable key={task.id} draggableId={task.id} index={index}>
                        {
                          (provided, snapshot) => (
                            <div ref={provided.innerRef}
                              {...provided.draggableProps}
                              {...provided.dragHandleProps}
                              style={{
                                ...provided.draggableProps.style,
                                opacity: snapshot.isDragging ? '0.5' : '1'
                              }}>
                              <Cards>
                                {task.title}
                              </Cards>

                            </div>
                          )
                        }
                      </Draggable>
                    ))}
                    {provided.placeholder}
                  </div>

                </div>
              )}
            </Droppable>
          ))
        }
      </div>

    </DragDropContext>
  )
}

export default DragDrop