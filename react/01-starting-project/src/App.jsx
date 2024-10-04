import Sidebar from "./components/Sidebar.jsx";
import Project from "./components/Project.jsx";
import NoProject from "./components/NoProject.jsx";
import { useState } from "react";

function App() {
  const [projectsState, setProjectState] = useState({
    selectedProjectId: undefined,
    projects: []
  })

  function handleStartAddProject() {
    setProjectState(prevState => {
      return {
        ...prevState,
        selectedProjectId: null
      }
    })
  }
  console.log(projectsState)
  function handleAddProject(projectData){
    setProjectState(prevState => {
      const newProject = {
        ...projectData,
        id: Math.random()
      }
      return {
        ...prevState,
        selectedProjectId: undefined,
        projects: [...prevState.projects, newProject]
      }
    })
  }

  let content
  if(projectsState.selectedProjectId === null) {
    content = <Project onAdd={handleAddProject}/>
  } else if(projectsState.selectedProjectId === undefined) {
    content = <NoProject onStartAddProject={handleStartAddProject}/>
  }
  return (
    <main className="h-screen my-8 flex gap-8">
      <Sidebar onStartAddProject={handleStartAddProject} projects={projectsState.projects}/>
      {content}
    </main>
  );
}

export default App;
