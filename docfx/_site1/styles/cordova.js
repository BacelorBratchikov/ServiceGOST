function clickUri(uri)
{
    viewDocument(uri, getMimeType(uri), 'click');
}

function viewDocument(url, mimeType, storage)
{
    if (!_sdv)
    {
        window.console.log("Attempting to view '" + url + "'");
        window.open(url);
        return false;
    }

    alert("Attempting to view '" + url + "'", view);


    function view()
    {
        var _autoClose;

        function onShow()
        {
            $('body').addClass('viewer_open');
            // shown
            window.console.log('document shown');

            if (autoCloseTimeoutSeconds > 0)
            {
                _autoClose = setTimeout(
                        function ()
                        {
                            _autoClose = null;
                            _sdv.closeDocument();
                        }, autoCloseTimeoutSeconds * 1000);
            }
        }

        function onClose()
        {
            if (_autoClose)
            {
                clearTimeout(_autoClose);
                _autoClose = null;
            }

            $('body').removeClass('viewer_open');
            // closed
            window.console.log('document closed');
        }


        var options = buildViewerOptions();
        options.title = url.split('/').pop() + '@' + storage;
        var linkHandlers = [
            {
                pattern: '^\/',
                close: false,
                handler: function (link) {
                    alert('link handler called with link: "' + link + '"');
                }
            },
            {
                pattern: '^\/',
                close: false,
                handler: function (link) {
                    alert('This handler should not be called because a prior handler should already have matched.');
                }
            },
            {
                pattern: '^\/order',
                close: false,
                handler: function (link) {
                    alert('This handler should not be called because a prior handler should already have matched.');
                }
            },
            {
                pattern: '[\s\S]*',
                close: true,
                handler: function (link) {
                    // catch-all handler demonstrating document close and regex pattern precedence
                }
            }
        ];

        _sdv.viewDocument(
                url,
                mimeType,
                options,
                onShow,
                onClose,
                function (appId, installer)
                {
                    $('body').removeClass('viewer_open');
                    // missing app
                    if (confirm("Do you want to install the free PDF Viewer App "
                                    + appId + " for Android?"))
                    {
                        installer(
                                function ()
                                {
                                    window.console.log(
                                            'successfully installed app');
                                    if (confirm("App installed. Do you want to view the document now?"))
                                        viewDocument(url, mimeType, storage);
                                },
                                function (error)
                                {
                                    window.console.log('cannot install app');
                                    window.console.log(error);
                                }
                        );
                    }
                },
                function (error)
                {
                    $('body').removeClass('viewer_open');
                    majorError('cannot view document ' + url, error);
                },
                linkHandlers
        );
    }

    return false;
}
