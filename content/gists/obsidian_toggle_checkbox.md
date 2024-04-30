+++
title = "📋obsidian_toggle_checkbox.md"
description = "A Templater template for quickly toggling between custom checkboxes using a hotkey."
date = 2024-05-01
draft = false

[taxonomies]
tags = ["obsidian", "templates", "markdown", "javascript"]

[extra]
# social_media_card = ""
+++

A [Templater](https://obsidian.md/plugins?search=templater) template for quickly toggling between [custom checkboxes](https://minimal.guide/checklists#Alternate+checkboxes) available in the [Minimal theme](https://minimal.guide/home) for [Obsidian](https://obsidian.md) using a hotkey.

> See original [showcase/discussion](https://github.com/SilentVoid13/Templater/discussions/1236).

```markdown
<%*
// List of all defined checkbox states. Adjust to match your setup.
// Remove "//" to enable additional states.
const states = {
	' ': 'Unchecked | Pending',
	'/': 'In Progress',
	'x': 'Checked | Done',
	'>': 'Rescheduled',
	'<': 'Scheduled',
	'-': 'Cancelled',
	// '':  'Clear Checkbox | Reset',
	// '!': 'Important',
	// '?': 'Question',
	// '*': 'Star',
	// 'n': 'Note',
	// 'l': 'Location',
	// 'i': 'Information',
	// 'I': 'Idea',
	// 'S': 'Amount | Price | Money',
	// 'p': 'Pro | Good',
	// 'c': 'Con | Bad',
	// 'b': 'Bookmark',
	// '"': 'Quote',
	// 'u': 'Up | Like',
	// 'd': 'Down | Dislike',
	// 'w': 'Win',
	// 'k': 'Key',
	// 'f': 'Fire | Hot'
};

// Whether to show the new-state input dialog.
// When set to false, the checkbox loops though all defined states.
let promptUser = false;

// Default state if this line: Undone checkbox.
// This state is used, if the current line is no checkbox yet, or if
// it's current state is unknown.
const defaultState = ' ';

// -- end of configuration.

// Helper functions.
const getLabel = key => (key ? `[${key}] ` : '') + `${states[key]}`;
const stateByListType = (listNumber, key) => key 
	? (listNumber ? `${listNumber} [${key}] ` : `- [${key}] `) 
	: ' ';
const setState = (key, line) => line.replace(
	/^(\s*)(-|\*|(\d\.))?(\s+\[.\])?\s*/,
	'$1$2' + stateByListType('$3', key)
);

// Prepare vars, inspect current editor line.
const stateKeys = Object.keys(states);
const editor = app.workspace.activeLeaf.view.editor;
const cursor = editor.getCursor('from');
const currentLine = editor.getLine(cursor.line);
const stateMatch = currentLine.match(/^[\s-\*]+\s\[(.)\]\s/);
const currentState = stateMatch?.[1] || '';
let newState = defaultState;

// We found a valid checkbox state. Let's find the next state in the queue.
if (currentState) {
	let nextIndex = stateKeys.indexOf(currentState) + 1
	if (nextIndex >= stateKeys.length) {
		nextIndex = 0;
	}
	newState = stateKeys[nextIndex];
}

// Optional branch: Let the user choose the new state.
if (promptUser) {
	// Display the "next state" as first option, so it's auto-selected.
	const suggestLabels = [getLabel(newState)];
	const suggestKeys = [newState];
	
	stateKeys.map(key => {
		if (key === newState) {
			return;
		}
		suggestLabels.push(getLabel(key))
		suggestKeys.push(key)
	});
	
	newState = await tp.system.suggester(
		suggestLabels,
		suggestKeys,
		false,
		"Select new checkbox state"
	);
}

if ('string' === typeof newState) {
	editor.setLine(cursor.line, setState(newState, currentLine));
}
%>
```
