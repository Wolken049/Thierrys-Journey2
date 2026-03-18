def shift():
        nonlocal InvTrig, CmdShift
        if not InvTrig:
            InvTrig = True
            Sin.config(text="sin⁻¹", command=lambda: click("sin⁻¹("))
            Cos.config(text="cos⁻¹", command=lambda: click("cos⁻¹("))
            Tan.config(text="tan⁻¹", command=lambda: click("tan⁻¹("))
        else:
            InvTrig = False
            Sin.config(text="sin", command=lambda: click("sin("))
            Cos.config(text="cos", command=lambda: click("cos("))
            Tan.config(text="tan", command=lambda: click("tan("))
        if not CmdShift:
            CmdShift = True
            Inverse.config(text="x!", command=lambda: click('!'))
        else:
            CmdShift = False        
            Inverse.config(text = "x⁻¹",command=lambda: click('⁻¹'))