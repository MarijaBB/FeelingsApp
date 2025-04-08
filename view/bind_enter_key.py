def bind_enter(part, function, *entry_widgets,root = None):
    part.bind('<Return>', lambda event: function(*(entry.get() for entry in entry_widgets), root))