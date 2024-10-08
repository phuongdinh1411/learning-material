import Button from "./Button.jsx";

export default function Sidebar({ onStartAddProject, projects }) {
  return (
    <aside className="w-1/3 px-8 py-16 bg-stone-900 text-stone-50">
      <h2 className="mb-8 font-bold uppercase md:text-xl text-stone-200">
        Your Project{" "}
      </h2>
      <div>
        <Button onClick={onStartAddProject}>+ Add Project</Button>
      </div>
      <ul className="mt-8">
        {projects.map((p) => (
          <li key={p.id}>
            <button className="w-full text-left px-2 py-1 rounded-sm my-1 text-stone-400 hover:text-slate-200 hover:bg-stone-800">{p.title}</button>
          </li>
        ))}
      </ul>
    </aside>
  );
}
