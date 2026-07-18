import { useState } from "react";
import {
    Plus,
    Pencil,
    Trash2,
    Calendar,
    ArrowDownCircle,
    ArrowUpCircle,
} from "lucide-react";

interface Transaction {
    id: number;
    title: string;
    category: string;
    amount: number;
    date: string;
    type: "income" | "expense";
}

const emptyTransaction: Omit<Transaction, "id"> = {
    title: "",
    category: "",
    amount: 0,
    date: "",
    type: "expense",
};

export default function TransactionsPanel() {
    const [transactions, setTransactions] = useState<Transaction[]>([
        {
            id: 1,
            title: "Salary",
            category: "Job",
            amount: 1200,
            date: "2026-07-02",
            type: "income",
        },
        {
            id: 2,
            title: "Steam Games",
            category: "Entertainment",
            amount: 70,
            date: "2026-07-05",
            type: "expense",
        },
        {
            id: 3,
            title: "Freelance",
            category: "Programming",
            amount: 420,
            date: "2026-07-09",
            type: "income",
        },
    ]);

    const [showAdd, setShowAdd] = useState(false);

    const [newTransaction, setNewTransaction] =
        useState<Omit<Transaction, "id">>(emptyTransaction);

    const [editingId, setEditingId] =
        useState<number | null>(null);

    const [editingTransaction, setEditingTransaction] =
        useState<Transaction | null>(null);

    const totalIncome = transactions
        .filter((t) => t.type === "income")
        .reduce((a, b) => a + b.amount, 0);

    const totalExpense = transactions
        .filter((t) => t.type === "expense")
        .reduce((a, b) => a + b.amount, 0);

    function addTransaction() {
        if (!newTransaction.title.trim()) return;

        setTransactions((prev) => [
            {
                id: Date.now(),
                ...newTransaction,
            },
            ...prev,
        ]);

        setNewTransaction(emptyTransaction);
        setShowAdd(false);
    }

    function deleteTransaction(id: number) {
        setTransactions((prev) =>
            prev.filter((t) => t.id !== id)
        );
    }

    function startEdit(transaction: Transaction) {
        setEditingId(transaction.id);
        setEditingTransaction({ ...transaction });
    }

    function saveEdit() {
        if (!editingTransaction) return;

        setTransactions((prev) =>
            prev.map((t) =>
                t.id === editingTransaction.id
                    ? editingTransaction
                    : t
            )
        );

        setEditingId(null);
        setEditingTransaction(null);
    }

    return (
        <div className="h-full p-8 text-gray-200">

            <div className="flex items-center justify-between mb-8">

                <div>
                    <h2 className="text-3xl font-bold text-start">
                        Transactions
                    </h2>

                    <p className="text-sm text-gray-400 mt-1">
                        Track your income and expenses.
                    </p>
                </div>

                <button
                    onClick={() => setShowAdd(!showAdd)}
                    className="rounded-xl bg-blue-600 px-4 py-2 hover:bg-blue-700 transition flex items-center gap-2"
                >
                    <Plus size={18} />
                    Add Transaction
                </button>

            </div>

            {/* Summary */}

            <div className="grid grid-cols-2 gap-5 mb-8">

                <div className="rounded-2xl border-2 border-zinc-700/80 bg-zinc-800 transition-translate duration-200 ease-in-out hover:scale-101 p-6">

                    <div className="flex items-center gap-3">

                        <ArrowUpCircle className="text-green-400" />

                        <span className="text-gray-400">
                            Total Income
                        </span>

                    </div>

                    <h3 className="mt-4 text-3xl font-bold text-green-400">

                        ${totalIncome}

                    </h3>

                </div>

                <div className="rounded-2xl border-2 border-zinc-700/80 bg-zinc-800 transition-translate duration-200 ease-in-out hover:scale-101 p-6">

                    <div className="flex items-center gap-3">

                        <ArrowDownCircle className="text-red-400" />

                        <span className="text-gray-400">
                            Total Expense
                        </span>

                    </div>

                    <h3 className="mt-4 text-3xl font-bold text-red-400">

                        ${totalExpense}

                    </h3>

                </div>

            </div>

            {/* Add Transaction */}

{showAdd && (
    <div className="mb-8 rounded-2xl border-2 border-zinc-700/80 bg-zinc-800 p-6">

        <h3 className="mb-6 text-xl font-semibold">
            New Transaction
        </h3>

        <div className="grid gap-4 md:grid-cols-2">

            <input
                type="text"
                placeholder="Title"
                value={newTransaction.title}
                onChange={(e) =>
                    setNewTransaction({
                        ...newTransaction,
                        title: e.target.value,
                    })
                }
                className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
            />

            <input
                type="text"
                placeholder="Category"
                value={newTransaction.category}
                onChange={(e) =>
                    setNewTransaction({
                        ...newTransaction,
                        category: e.target.value,
                    })
                }
                className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
            />

            <input
                type="number"
                placeholder="Amount"
                value={
                    newTransaction.amount === 0
                        ? ""
                        : newTransaction.amount
                }
                onChange={(e) =>
                    setNewTransaction({
                        ...newTransaction,
                        amount: Number(e.target.value),
                    })
                }
                className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
            />

            <input
                type="date"
                value={newTransaction.date}
                onChange={(e) =>
                    setNewTransaction({
                        ...newTransaction,
                        date: e.target.value,
                    })
                }
                className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
            />

            <select
                value={newTransaction.type}
                onChange={(e) =>
                    setNewTransaction({
                        ...newTransaction,
                        type: e.target.value as
                            | "income"
                            | "expense",
                    })
                }
                className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
            >
                <option value="expense">
                    💸 Expense
                </option>

                <option value="income">
                    💰 Income
                </option>

            </select>

        </div>

        <div className="mt-6 flex gap-3">

            <button
                onClick={addTransaction}
                className="rounded-xl bg-blue-600 px-6 py-3 font-medium transition hover:bg-blue-700"
            >
                Save Transaction
            </button>

            <button
                onClick={() => {
                    setShowAdd(false);
                    setNewTransaction(emptyTransaction);
                }}
                className="rounded-xl bg-zinc-900 px-6 py-3 font-medium transition hover:bg-zinc-700"
            >
                Cancel
            </button>

        </div>

    </div>
)}
            <div className="space-y-5"></div>
{transactions.map((transaction) => (
    <div
        key={transaction.id}
        className={`group overflow-hidden rounded-2xl border-2 border-zinc-700/80 bg-zinc-800 mb-3 transition-all duration-300 hover:scale-[1.005]`}
    >
        {editingId === transaction.id && editingTransaction ? (
            <div className="space-y-4 p-6">

                <input
                    value={editingTransaction.title}
                    onChange={(e) =>
                        setEditingTransaction({
                            ...editingTransaction,
                            title: e.target.value,
                        })
                    }
                    className="w-full rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
                    placeholder="Title"
                />

                <input
                    value={editingTransaction.category}
                    onChange={(e) =>
                        setEditingTransaction({
                            ...editingTransaction,
                            category: e.target.value,
                        })
                    }
                    className="w-full rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
                    placeholder="Category"
                />

                <input
                    type="number"
                    value={editingTransaction.amount}
                    onChange={(e) =>
                        setEditingTransaction({
                            ...editingTransaction,
                            amount: Number(e.target.value),
                        })
                    }
                    className="w-full rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
                />

                <input
                    type="date"
                    value={editingTransaction.date}
                    onChange={(e) =>
                        setEditingTransaction({
                            ...editingTransaction,
                            date: e.target.value,
                        })
                    }
                    className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500 mr-2"
                />

                <select
                    value={editingTransaction.type}
                    onChange={(e) =>
                        setEditingTransaction({
                            ...editingTransaction,
                            type: e.target.value as
                                | "income"
                                | "expense",
                        })
                    }
                    className="rounded-xl bg-zinc-900 px-4 py-3 outline-none ring-1 ring-transparent transition focus:ring-blue-500"
                >
                    <option value="income">
                        Income
                    </option>

                    <option value="expense">
                        Expense
                    </option>

                </select>

                <div className="flex gap-3">

                    <button
                        onClick={saveEdit}
                        className="rounded-xl bg-green-600 px-5 py-2 hover:bg-green-700"
                    >
                        Save
                    </button>

                    <button
                        onClick={() => {
                            setEditingId(null);
                            setEditingTransaction(null);
                        }}
                        className="rounded-xl bg-zinc-700 px-5 py-2"
                    >
                        Cancel
                    </button>

                </div>

            </div>
        ) : (
            <div className="flex items-center justify-between py-1 px-5">

                <div className="flex items-center gap-5">

                    <div
                        className={`flex p-1 items-center justify-center rounded-full
                        ${
                            transaction.type === "income"
                                ? "bg-green-500/15"
                                : "bg-red-500/15"
                        }`}
                    >
                        {transaction.type === "income" ? (
                            <ArrowUpCircle
                                className="text-green-400"
                                size={28}
                            />
                        ) : (
                            <ArrowDownCircle
                                className="text-red-400"
                                size={28}
                            />
                        )}
                    </div>

                    <div>

                        <h3 className="font-semibold text-lg text-start">

                            {transaction.title}

                        </h3>

                        <div className="mt-2 flex items-center gap-3">

                            <span className="rounded-full bg-zinc-800 px-3 py-1 text-xs text-gray-300">

                                {transaction.category}

                            </span>

                            <div className="flex items-center gap-1 text-xs text-gray-500">

                                <Calendar size={14} />

                                {transaction.date}

                            </div>

                        </div>

                    </div>

                </div>

                <div className="flex items-center gap-6">

                    <span
                        className={`text-2xl font-bold
                        ${
                            transaction.type === "income"
                                ? "text-green-400"
                                : "text-red-400"
                        }`}
                    >
                        {transaction.type === "income"
                            ? "+"
                            : "-"}
                        ${transaction.amount}
                    </span>

                    <div className="flex gap-2 opacity-0 transition group-hover:opacity-100">

                        <button
                            onClick={() =>
                                startEdit(transaction)
                            }
                            className="rounded-lg p-2 hover:bg-zinc-900"
                        >
                            <Pencil size={18} />
                        </button>

                        <button
                            onClick={() =>
                                deleteTransaction(
                                    transaction.id
                                )
                            }
                            className="rounded-lg p-2 hover:bg-red-600"
                        >
                            <Trash2 size={18} />
                        </button>

                    </div>

                </div>

            </div>
        )}
    </div>
))}

</div>

);
}