Android Development Gotchas
=====

An unordered list of counter-intuitive problems and hard-won solutions (that sort of thing) for Android Development.



Get Target Context During Instrumented (on-phone) Tests
------

How to get the same `Context` as your app under test was oddly hard for me, since the API 23 update.



In a method annotated with `@Test` or `@Before`:

```java

import android.support.test.InstrumentationRegistry;
import android.content.Context;

public class TestWithContext {

...

	@Before
    public void before() {
	Context context = InstrumentationRegistry.getTargetContext();
	}
}
```

Waiting for some time in Android
---

###(instead of Java's `Thread.sleep(long ms)` )

This [hidden gem](https://developer.android.com/reference/android/os/SystemClock.html) says to do this:

```
SystemClock.sleep(long ms)
```
