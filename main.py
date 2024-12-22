import gifos

def main():
    t = gifos.Terminal(width=750, height=500, xpad=15, ypad=15)
    t.set_prompt("[user@localhost ~]# ")
    t.set_fps(20)

    t.gen_prompt(1, count=15)
    t.toggle_show_cursor(True)
    t.gen_typing_text("ls", 1, contin=True)
    t.toggle_show_cursor(False)
    t.clone_frame(5)

    t.gen_text("""Desktop    Documents    Downloads    Music    Pictures
me.txt
""", row_num=2)
    
    t.gen_prompt(row_num=5, count=20)
    t.toggle_show_cursor(True)

    t.gen_typing_text("cat me.txt", row_num=5, contin=True)
    t.toggle_show_cursor(False)
    t.clone_frame(5)

    t.gen_text("""User: Thomas Cabovianco
School: University of Buenos Aires [UBA]
Major: Computer Engineering [In Progress]
Interests: Programming, Linux, Cybersecurity, Mobile Development
"""
    , row_num=6)

    t.gen_prompt(row_num=11, count=120)
    t.toggle_show_cursor(True)
    t.gen_typing_text("clear", row_num=11, contin=True, speed=3)
    t.toggle_show_cursor(False)

    t.clear_frame()
    t.gen_gif()

if __name__ == "__main__":
    main()
