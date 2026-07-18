export default function Header(){
    return(
        <header className="flex flex-row px-10 py-6">
            <div id="name" className="flex items-center basis-1/3">
                <div 
                className="
                    dark:bg-white bg-black rounded-md w-content
                    px-[8px] py-[2px] mr-2 dark:text-black text-white
                    font-bold"
                >H</div>
                <p className="text-h text-[var(--text-h)] font-bold">HABER</p>
            </div>
            <nav className="flex basis-1/3 justify-center items-center">
                <ul className="flex flex-row gap-x-10 justify-center content-center">
                    <li className="text hover:scale-125">Product</li>
                    <li className="text hover:scale-125">Blog</li>
                    <li className="text hover:scale-125">About us</li>
                </ul>
            </nav>
            <div id="sign-in-bottun" className="basis-1/3 items-center flex justify-end">
                <a 
                href="/auth" 
                className="dark:text-black text-white bg-black dark:bg-white
                    p-2 rounded-3xl px-4 font-bold
                "
                >
                    Sign up | Sign in
                </a>
            </div>
        </header>
    );
}