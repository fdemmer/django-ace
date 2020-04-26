(function () {
  function getDocHeight() {
    let D = document;
    return Math.max(
      Math.max(D.body.scrollHeight, D.documentElement.scrollHeight),
      Math.max(D.body.offsetHeight, D.documentElement.offsetHeight),
      Math.max(D.body.clientHeight, D.documentElement.clientHeight)
    );
  }

  function getDocWidth() {
    let D = document;
    return Math.max(
      Math.max(D.body.scrollWidth, D.documentElement.scrollWidth),
      Math.max(D.body.offsetWidth, D.documentElement.offsetWidth),
      Math.max(D.body.clientWidth, D.documentElement.clientWidth)
    );
  }

  function next(elem) {
    // Credit to John Resig for this function
    // taken from Pro JavaScript techniques
    do {
      elem = elem.nextSibling;
    } while (elem && elem.nodeType != 1);
    return elem;
  }

  function prev(elem) {
    // Credit to John Resig for this function
    // taken from Pro JavaScript techniques
    do {
      elem = elem.previousSibling;
    } while (elem && elem.nodeType != 1);
    return elem;
  }

  function minimizeMaximize(widget, main_block, editor) {
    if (window.fullscreen == true) {
      main_block.className = "django-ace-editor";

      widget.style.width = window.ace_widget.width + "px";
      widget.style.height = window.ace_widget.height + "px";
      widget.style.zIndex = 1;
      window.fullscreen = false;
    } else {
      window.ace_widget = {
        width: widget.offsetWidth,
        height: widget.offsetHeight,
      };

      main_block.className = "django-ace-editor-fullscreen";

      widget.style.height = getDocHeight() + "px";
      widget.style.width = getDocWidth() + "px";
      widget.style.zIndex = 999;

      window.scrollTo(0, 0);
      window.fullscreen = true;
      editor.resize();
    }
  }

  function apply_widget(widget) {
    let div = widget.firstChild,
      textarea = next(widget),
      mode = widget.getAttribute("data-mode"),
      theme = widget.getAttribute("data-theme"),
      useWorker = widget.hasAttribute("data-use-worker"),
      useWrapMode = widget.hasAttribute("data-wrap-mode"),
      minLines = widget.getAttribute("data-min-lines"),
      maxLines = widget.getAttribute("data-max-lines"),
      showPrintMargin = widget.hasAttribute("data-show-print-margin"),
      showInvisibles = widget.hasAttribute("data-show-invisibles"),
      tabSize = widget.getAttribute("data-tab-size"),
      fontSize = widget.getAttribute("data-font-size"),
      useSoftTabs = widget.hasAttribute("data-use-soft-tabs"),
      toolbar = prev(widget);

    // initialize editor and attach to widget element (for use in formset:removed)
    let editor = (widget.editor = ace.edit(div, {
      useWorker: useWorker,
      showPrintMargin: showPrintMargin,
      showInvisibles: showInvisibles,
    }));

    let main_block = div.parentNode.parentNode;
    if (toolbar != null) {
      // Toolbar maximize/minimize button
      let min_max = toolbar.getElementsByClassName("django-ace-max_min");
      min_max[0].onclick = function () {
        minimizeMaximize(widget, main_block, editor);
        return false;
      };
    }

    // load initial data
    editor.session.setValue(textarea.value);

    // the editor is initially absolute positioned
    textarea.style.display = "none";

    // options
    if (mode) {
      editor.session.setMode("ace/mode/" + mode);
    }
    if (theme) {
      editor.setTheme("ace/theme/" + theme);
    }
    if (!!minLines) {
      editor.setOption("minLines", minLines);
    }
    if (!!maxLines) {
      editor.setOption("maxLines", maxLines == "-1" ? Infinity : maxLines);
    }
    if (!!tabSize) {
      editor.setOption("tabSize", tabSize);
    }
    if (!!fontSize) {
      editor.setOption("fontSize", fontSize);
    }
    editor.session.setUseSoftTabs(useSoftTabs);
    editor.session.setUseWrapMode(useWrapMode);

    // write data back to original textarea
    editor.session.on("change", function () {
      textarea.value = editor.session.getValue();
    });

    editor.commands.addCommand({
      name: "Full screen",
      bindKey: { win: "Ctrl-F11", mac: "Command-F11" },
      exec: function (editor) {
        minimizeMaximize(widget, main_block, editor);
      },
      readOnly: true, // false if this command should not apply in readOnly mode
    });
  }

  /**
   * Determine if the given element is within the element that holds the template
   * for dynamically added forms for an InlineModelAdmin.
   *
   * @param {*} widget - The element to check.
   */
  function is_empty_form(widget) {
    let empty_forms = document.getElementsByClassName("empty-form");
    for (empty_form of empty_forms) {
      if (empty_form.contains(widget)) {
        return true;
      }
    }
    return false;
  }

  function init() {
    let widgets = document.getElementsByClassName("django-ace-widget");
    for (widget of widgets) {
      // skip the widget in the admin inline empty-form
      if (is_empty_form(widget)) {
        continue;
      }
      // skip already loaded widgets
      if (!widget.classList.contains("loading")) {
        continue;
      }
      widget.className = "django-ace-widget"; // remove `loading` class
      apply_widget(widget);
    }
  }

  // Django's jQuery instance is available, we are probably in the admin
  if (typeof django == "object") {
    django.jQuery(document).on("formset:added", function (event, $row, formsetName) {
      // Row added to InlineModelAdmin, initialize new widgets
      init();
    });
    django.jQuery(document).on("formset:removed", function (event, $row, formsetName) {
      // Row removed from InlineModelAdmin, destroy attached editor
      $row.find("div.django-ace-widget")[0].editor.destroy();
    });
  }

  if (window.addEventListener) {
    // W3C
    window.addEventListener("load", init);
  } else if (window.attachEvent) {
    // Microsoft
    window.attachEvent("onload", init);
  }
})();
