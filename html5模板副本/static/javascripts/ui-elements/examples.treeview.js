
(function( $ ) {

	'use strict';

	/*
	Basic
	*/
	$('#treeBasic').jstree({
		'core' : {
			'themes' : {
				'responsive': false
			}
		},
		'types' : {
			'default' : {
				'icon' : 'fa fa-folder'
			},
			'file' : {
				'icon' : 'fa fa-file'
			}
		},
		'plugins': ['types']
	});

	/*
	Checkbox
	*/
	$('#treeCheckbox').jstree({
		'core' : {
			'themes' : {
				'responsive': false
			}
		},
		'types' : {
			'default' : {
				'icon' : 'fa fa-folder'
			},
			'file' : {
				'icon' : 'fa fa-file'
			}
		},
		'plugins': ['types', 'checkbox']
	});

	/*
	Ajax HTML
	*/
	$('#treeAjaxHTML').jstree({
		'core' : {
			'themes' : {
				'responsive': false
			}, 
			'check_callback' : true,
			'data' : {
				'url' : function (node) {
				  return 'static/ajax/ajax-treeview-nodes.html';
				},
				'data' : function (node) {
				  return { 'parent' : node.id };
				}
			}
		},
		'types' : {
			'default' : {
				'icon' : 'fa fa-folder'
			},
			'file' : {
				'icon' : 'fa fa-file'
			}
		},
		'plugins': ['types']
	});

	/*
	Ajax JSON
	*/
	$('#treeAjaxJSON').jstree({
		'core' : {
			'themes' : {
				'responsive': false
			}, 
			'check_callback' : true,
			'data' : {
				'url' : function (node) {
					return node.id === '#' ? 'static/ajax/ajax-treeview-roots.json' : 'static/ajax/ajax-treeview-children.json';
				},
				'data' : function (node) {
					return { 'id' : node.id };
				}
			}
		},
		'types' : {
			'default' : {
				'icon' : 'fa fa-folder'
			},
			'file' : {
				'icon' : 'fa fa-file'
			}
		},
		'plugins': ['types']
	});

	/*
	Drag & Drop
	*/
	$('#treeDragDrop').jstree({
		'core' : {
			'check_callback' : true,
			'themes' : {
				'responsive': false
			}
		},
		'types' : {
			'default' : {
				'icon' : 'fa fa-folder'
			},
			'file' : {
				'icon' : 'fa fa-file'
			}
		},
		'plugins': ['types', 'dnd']
	});

}).apply( this, [ jQuery ]);