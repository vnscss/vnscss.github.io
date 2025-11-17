var { 
        OverlayScrollbars, 
        ScrollbarsHidingPlugin, 
        SizeObserverPlugin, 
        ClickScrollPlugin  
    } = OverlayScrollbarsGlobal;
const osInstance = OverlayScrollbars(document.getElementById('scroll-area'), {			
        paddingAbsolute: false,
        showNativeOverlaidScrollbars: false,
        update: {
            elementEvents: [['img', 'load']],
            debounce: [0, 33],
            attributes: null,
            ignoreMutation: null,
        },
        overflow: {
            x: 'scroll',
            y: 'scroll',
        },
        scrollbars: {
            theme: 'os-theme-dark',
            visibility: 'auto',
            autoHide: 'scroll',
            autoHideDelay: 1300,
            autoHideSuspend: false,
            dragScroll: true,
            clickScroll: false,
            pointers: ['mouse', 'touch', 'pen'],
        },});