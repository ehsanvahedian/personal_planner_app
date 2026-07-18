import { useState } from "react";
import {
    Plus,
    Pencil,
    Trash2,
    CheckCircle2,
    Circle,
    Calendar,
} from "lucide-react";

interface Task {
    id: number;
    title: string;
    description: string;
    due: string;
    completed: boolean;
}

const emptyTask: Omit<Task, "id" | "completed"> = {
    title: "",
    description: "",
    due: "",
};

export default function TasksPanel() {
    const [tasks, setTasks] = useState<Task[]>([
        {
            id: 1,
            title: "Finish Dashboard UI",
            description: "Design the dashboard page.",
            due: "2026-07-20",
            completed: false,
        },
        {
            id: 2,
            title: "Connect FastAPI",
            description: "Implement CRUD APIs.",
            due: "2026-07-22",
            completed: true,
        },
        {
            id: 3,
            title: "Write README",
            description: "Project documentation.",
            due: "2026-07-25",
            completed: false,
        },
    ]);

    const [showAdd, setShowAdd] = useState(false);

    const [newTask, setNewTask] =
        useState<Omit<Task, "id" | "completed">>(emptyTask);

    const [editingId, setEditingId] = useState<number | null>(null);

    const [editingTask, setEditingTask] =
        useState<Task | null>(null);

    function addTask() {
        if (!newTask.title.trim()) return;

        const task: Task = {
            id: Date.now(),
            completed: false,
            ...newTask,
        };

        setTasks((prev) => [task, ...prev]);

        setNewTask(emptyTask);
        setShowAdd(false);
    }

    function deleteTask(id: number) {
        setTasks((prev) => prev.filter((t) => t.id !== id));
    }

    function toggleCompleted(id: number) {
        setTasks((prev) =>
            prev.map((t) =>
                t.id === id
                    ? {
                          ...t,
                          completed: !t.completed,
                      }
                    : t
            )
        );
    }

    function startEdit(task: Task) {
        setEditingId(task.id);
        setEditingTask({ ...task });
    }

    function saveEdit() {
        if (!editingTask) return;

        setTasks((prev) =>
            prev.map((t) =>
                t.id === editingTask.id
                    ? editingTask
                    : t
            )
        );

        setEditingId(null);
        setEditingTask(null);
    }

    return (
        <div className="h-full p-8 text-gray-200">

            {/* Header */}

            <div className="mb-8 flex items-center justify-between">

                <div>
                    <h2 className="text-3xl font-bold text-start">
                        Tasks
                    </h2>

                    <p className="mt-1 text-sm text-gray-400">
                        Manage your daily work.
                    </p>
                </div>

                <button
                    onClick={() => setShowAdd(!showAdd)}
                    className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 hover:bg-blue-700 transition"
                >
                    <Plus size={18} />
                    Add Task
                </button>

            </div>

            {/* Add Task */}

            {showAdd && (
                <div className="mb-8 space-y-4 rounded-xl border-2 border-zinc-700/80 bg-zinc-800 p-5">

                    <input
                        className="w-full rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700"
                        placeholder="Task title"
                        value={newTask.title}
                        onChange={(e) =>
                            setNewTask({
                                ...newTask,
                                title: e.target.value,
                            })
                        }
                    />

                    <textarea
                        rows={3}
                        className="w-full rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700"
                        placeholder="Description"
                        value={newTask.description}
                        onChange={(e) =>
                            setNewTask({
                                ...newTask,
                                description:
                                    e.target.value,
                            })
                        }
                    />

                    <input
                        type="date"
                        className="rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700 mr-3"
                        value={newTask.due}
                        onChange={(e) =>
                            setNewTask({
                                ...newTask,
                                due: e.target.value,
                            })
                        }
                    />

                    <button
                        onClick={addTask}
                        className="rounded-lg bg-green-600 px-5 py-2 hover:bg-green-700 transition mr-3"
                    >
                        Save
                    </button>

                    <button
                        onClick={() => setShowAdd(false)}
                        className="rounded-lg bg-zinc-700 px-5 py-2 hover:bg-zinc-600 transition"
                    >
                        Cancel
                    </button>

                </div>
            )}

            {/* Task List */}

            <div className="space-y-5">
                {tasks.map((task) => (
                    <div
                        key={task.id}
                        className="group overflow-hidden rounded-xl border border-zinc-800 bg-zinc-800"
                    >
                        {editingId === task.id && editingTask ? (
                            <div className="space-y-4 p-5">

                                <input
                                    className="w-full rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700 mr-3"
                                    value={editingTask.title}
                                    onChange={(e) =>
                                        setEditingTask({
                                            ...editingTask,
                                            title: e.target.value,
                                        })
                                    }
                                />

                                <textarea
                                    rows={3}
                                    className="w-full rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700 mr-3"
                                    value={editingTask.description}
                                    onChange={(e) =>
                                        setEditingTask({
                                            ...editingTask,
                                            description: e.target.value,
                                        })
                                    }
                                />

                                <input
                                    type="date"
                                    className="rounded-lg bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent focus:ring-blue-700 mr-3"
                                    value={editingTask.due}
                                    onChange={(e) =>
                                        setEditingTask({
                                            ...editingTask,
                                            due: e.target.value,
                                        })
                                    }
                                />

                                <div className="flex gap-3">

                                    <button
                                        onClick={saveEdit}
                                        className="rounded-lg bg-green-600 px-5 py-2 hover:bg-green-700 transition"
                                    >
                                        Save
                                    </button>

                                    <button
                                        onClick={() => {
                                            setEditingId(null);
                                            setEditingTask(null);
                                        }}
                                        className="rounded-lg bg-zinc-700 px-5 py-2 hover:bg-zinc-600 transition"
                                    >
                                        Cancel
                                    </button>

                                </div>

                            </div>
                        ) : (
                            <div className="flex items-center justify-between gap-6 py-2 px-5">

                                <div className="flex gap-4">

                                    <button
                                        onClick={() =>
                                            toggleCompleted(task.id)
                                        }
                                        className="mt-1"
                                    >
                                        {task.completed ? (
                                            <CheckCircle2
                                                size={24}
                                                className="text-green-500"
                                            />
                                        ) : (
                                            <Circle
                                                size={24}
                                                className="text-gray-500"
                                            />
                                        )}
                                    </button>

                                    <div>

                                        <h3
                                            className={`text-lg font-semibold ${
                                                task.completed
                                                    ? "text-gray-500 line-through"
                                                    : ""
                                            }`}
                                        >
                                            {task.title}
                                        </h3>

                                        <p className="mt-2 text-sm text-gray-400">
                                            {task.description}
                                        </p>

                                        <div className="mt-4 flex items-center gap-2 text-sm text-gray-500">

                                            <Calendar size={16} />

                                            <span>
                                                {task.due || "No deadline"}
                                            </span>

                                        </div>

                                    </div>

                                </div>

                                <div className="flex gap-2 opacity-0 transition group-hover:opacity-100">

                                    <button
                                        onClick={() =>
                                            startEdit(task)
                                        }
                                        className="rounded-lg p-2 hover:bg-zinc-900"
                                    >
                                        <Pencil size={18} />
                                    </button>

                                    <button
                                        onClick={() =>
                                            deleteTask(task.id)

                                        }
                                        className="rounded-lg p-2 hover:bg-red-600"
                                    >
                                        <Trash2 size={18} />
                                    </button>

                                </div>
                            </div>
                        )}
                    </div>
                ))}
            </div>

        </div>
    );
}