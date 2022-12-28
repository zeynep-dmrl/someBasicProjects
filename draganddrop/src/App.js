import DragDrop from "./components/DragDrop";
import './App.scss'

function App() {
  return (
    <div>
      <div style={{ padding: '50px' }}>
        <div  className="header"><b>ToDo App</b></div>
        <DragDrop/>
      </div>
    </div>
  );
}

export default App;
