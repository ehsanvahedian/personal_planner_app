import { useState } from "react"
import { Document_icon, Task_icon, Transaction_icon } from "./icons"
import TasksPanel from "./task_panel"
import TransactionsPanel from "./transaction_panel"
export default function Panel_preview(){
    const modes = ["Tasks", "Transactions", "Documents"]
    const [dashMenu , setDashMenu] = useState<String>(modes[0])
    return(
        <div
        className="
        rounded-4xl shadow-2xl bg-zinc-800 border border-zinc-700
        overflow-hidden
        ">
            <div className="flex flex-row p-2 pl-5 ">
                <div className="basis-1/3 flex flex-row gap-2 items-center">
                    <span className="w-[13px] h-[13px] bg-red-500/80 rounded-full"></span>
                    <span className="w-[13px] h-[13px] bg-yellow-500/80 rounded-full"></span>
                    <span className="w-[13px] h-[13px] bg-green-500/80 rounded-full"></span>
                </div>
                <p className="text-zinc-400 font-bold basis-1/3">Dashboard</p>
            </div>
            <div className="flex flex-row min-h-[60vh] max-h-[60vh] overflow-hidden">
                <div className="border-t border-r border-zinc-700 p-5 basis-1/4">
                    <p className="w-full text-left font-bold text-zinc-400">WORKSPACE</p>
                    <div className="pt-5">
                    {
                        modes.map
                        (i => 
                                <div 
                                className={`flex flex-row px-3 py-2 gap-3 rounded-2xl mt-3 cursor-pointer ${i==dashMenu?'border border-blue-600/60 bg-blue-600/13':''}`}
                                onClick={() => setDashMenu(i)}
                                >
                                    <span className={i==dashMenu?'text-blue-600':'text-zinc-400'}>
                                        {i=="Tasks" ? <Task_icon /> : i == "Transactions" ? <Transaction_icon /> : <Document_icon />}
                                    </span>
                                    <p className={i==dashMenu?"":"text-zinc-400"}>{i}</p>
                                </div>
                        )
                    }
                    </div>
                </div>
                <div className="border-t border-zinc-700 bg-zinc-900 basis-3/4 overflow-scroll">
                    {

                    <>
                        {dashMenu=="Tasks" ? <TasksPanel /> : dashMenu == "Transactions" ? <TransactionsPanel />: <Document_icon />}
                    
                    </>
                        
                    }
                </div>
            </div>
        </div>
    )
} 