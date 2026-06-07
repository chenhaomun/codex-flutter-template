---
name: test-driven-development
description: Automatically use test-driven development for clear behavior changes, even when the user does not explicitly ask for TDD. Trigger for bug fixes, validation rules, business logic, parser/mapper behavior, repository/use-case behavior, Bloc/Cubit state transitions, and user-flow logic where the expected result can be expressed as a focused failing test before implementation.
---

# Test Driven Development

Use TDD automatically when expected behavior is clear enough to test. Do not wait for the user to say "TDD" or invoke this skill explicitly.

Do not use strict TDD for trivial UI styling, copy/theme/config edits, generated files, exploratory refactors, or ambiguous requirements.

Project conventions win over examples. Use existing test libraries, helpers, mocks, fixtures, naming, and folder layout.

## Loop

| Step | Action |
|---|---|
| 1. Behavior | State the exact behavior under test in one sentence |
| 2. Red | Add/update the smallest failing test that proves the behavior is missing or broken |
| 3. Run narrow | Run only the new/changed test first |
| 4. Green | Implement the smallest project-compatible change to pass |
| 5. Refactor | Clean duplication or naming only after the test passes |
| 6. Verify | Re-run the focused test, then the narrow relevant analyzer/test command |

If the test cannot be written because requirements are unclear, stop and ask BA/TL for clarification instead of guessing.

## Test Choice

| Behavior | Prefer |
|---|---|
| Pure Dart rules, mappers, validators, use cases | Unit test |
| Bloc/Cubit events, commands, states | Bloc/Cubit unit test using existing project pattern |
| Repository behavior with API/cache dependency | Unit test with existing mock/fake style |
| Widget rendering or interaction | Widget test |
| Full navigation/user flow | Integration test only when existing or requested |

Do not introduce a new mocking package, state test package, golden test tool, or integration harness without approval.

## Red Examples

### Validator

Behavior: empty email must return an actionable validation error.

```dart
test('returns error when email is empty', () {
  final result = validateEmail('');

  expect(result, EmailValidationError.empty);
});
```

Then implement the smallest validation branch needed to pass.

### Bloc/Cubit State

Behavior: login failure emits an error state and stops loading.

```dart
blocTest<LoginCubit, LoginState>(
  'emits failure state when login request fails',
  build: () {
    when(authRepository.login(any, any)).thenThrow(AuthException('Invalid login'));
    return LoginCubit(authRepository);
  },
  act: (cubit) => cubit.login('a@b.com', 'bad-password'),
  expect: () => [
    const LoginState.loading(),
    const LoginState.failure('Invalid login'),
  ],
);
```

Match the project's actual bloc/cubit test helpers and state constructors.

### Repository Mapper

Behavior: API response maps nullable display name to fallback username.

```dart
test('uses username when displayName is null', () {
  final dto = UserDto.fromJson({
    'id': 'u1',
    'username': 'haomu',
    'displayName': null,
  });

  expect(dto.toDomain().name, 'haomu');
});
```

Then update only the mapper or model boundary that owns the rule.

### Widget Interaction

Behavior: tapping retry calls the retry callback from the error view.

```dart
testWidgets('calls retry when retry button is tapped', (tester) async {
  var retryCount = 0;

  await tester.pumpWidget(
    MaterialApp(
      home: ErrorView(onRetry: () => retryCount++),
    ),
  );

  await tester.tap(find.text('Retry'));
  await tester.pump();

  expect(retryCount, 1);
});
```

Prefer project keys/components over text finders when the app already has stable test selectors.

## Report

When done, report:

| Field | Content |
|---|---|
| TDD | used / skipped with reason |
| Red test | file and behavior |
| Verification | focused test and final narrow check |
| Gaps | untested risk or blocker |
